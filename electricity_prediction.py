"""
XGBoost를 활용한 전력사용량 예측
"""

# Import
import random
import pandas as pd
import numpy as np
import os

from xgboost import XGBRegressor

import warnings
warnings.filterwarnings(action='ignore')


# Fixed RandomSeed
def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)


seed_everything(42)  # Seed 고정


# Load Data & Pre-Processing
print("Loading data...")
train_df = pd.read_csv('./elec_2025_data/train.csv')
test_df = pd.read_csv('./elec_2025_data/test.csv')

print(f"Train data shape: {train_df.shape}")
print(f"Test data shape: {test_df.shape}")

# 시계열 특성을 학습에 반영하기 위해 일시를 월, 일, 시간으로 나눕니다
print("\nProcessing time features...")
train_df['month'] = train_df['일시'].apply(lambda x: int(x[4:6]))
train_df['day'] = train_df['일시'].apply(lambda x: int(x[6:8]))
train_df['time'] = train_df['일시'].apply(lambda x: int(x[9:11]))

train_x = train_df.drop(columns=['num_date_time', '일시', '일조(hr)', '일사(MJ/m2)', '전력소비량(kWh)'])
train_y = train_df['전력소비량(kWh)']

# 시계열 특성을 학습에 반영하기 위해 test 데이터도 동일하게 처리합니다
test_df['month'] = test_df['일시'].apply(lambda x: int(x[4:6]))
test_df['day'] = test_df['일시'].apply(lambda x: int(x[6:8]))
test_df['time'] = test_df['일시'].apply(lambda x: int(x[9:11]))

test_x = test_df.drop(columns=['num_date_time', '일시'])

print(f"Train X shape: {train_x.shape}")
print(f"Train Y shape: {train_y.shape}")
print(f"Test X shape: {test_x.shape}")


# Train
print("\nTraining XGBoost model...")
model = XGBRegressor()
model.fit(train_x, train_y)
print("Training completed!")


# Prediction
print("\nMaking predictions...")
preds = model.predict(test_x)
print(f"Predictions shape: {preds.shape}")


# Submission
print("\nCreating submission file...")
submission = pd.read_csv('./elec_2025_data/sample_submission.csv')
submission['answer'] = preds

submission.to_csv('./baseline_submission.csv', index=False)
print("Submission file saved as 'baseline_submission.csv'")
print("\nDone!")
