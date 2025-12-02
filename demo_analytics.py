"""
demo_analytics.py - Minimal demo script showcasing key library operations

This script demonstrates that all upgraded dependencies work correctly
for common analytics tasks.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy import stats


def main():
    print("=" * 60)
    print("Analytics Service Demo - Dependency Validation")
    print("=" * 60)
    print()
    
    # 1. Generate sample data with numpy
    print("📊 Generating sample data with NumPy...")
    np.random.seed(42)
    X_raw = np.random.uniform(0, 100, 200)
    noise = np.random.normal(0, 10, 200)
    y_raw = 2.5 * X_raw + 30 + noise
    print(f"   Generated {len(X_raw)} data points")
    print()
    
    # 2. Process data with pandas
    print("🐼 Processing data with Pandas...")
    df = pd.DataFrame({
        'feature': X_raw,
        'target': y_raw
    })
    
    # Add derived features
    df['feature_squared'] = df['feature'] ** 2
    df['feature_log'] = np.log1p(df['feature'])
    
    print(f"   DataFrame shape: {df.shape}")
    print(f"   Target mean: {df['target'].mean():.2f}")
    print(f"   Target std: {df['target'].std():.2f}")
    print()
    
    # 3. Statistical analysis with scipy
    print("📈 Running statistical analysis with SciPy...")
    correlation, p_value = stats.pearsonr(df['feature'], df['target'])
    print(f"   Pearson correlation: {correlation:.4f}")
    print(f"   P-value: {p_value:.6f}")
    print()
    
    # 4. Machine learning with scikit-learn
    print("🤖 Training model with Scikit-Learn...")
    X = df[['feature']].values
    y = df['target'].values
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    print(f"   Model coefficient: {model.coef_[0]:.4f}")
    print(f"   Model intercept: {model.intercept_:.4f}")
    print(f"   Training R²: {train_score:.4f}")
    print(f"   Testing R²: {test_score:.4f}")
    print()
    
    # 5. Visualization with matplotlib
    print("📊 Creating visualization with Matplotlib...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Scatter plot with regression line
    ax1.scatter(X_test, y_test, alpha=0.5, label='Test Data')
    X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = model.predict(X_line)
    ax1.plot(X_line, y_line, 'r-', linewidth=2, label='Regression Line')
    ax1.set_xlabel('Feature')
    ax1.set_ylabel('Target')
    ax1.set_title('Linear Regression Results')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Residual plot
    y_pred = model.predict(X_test)
    residuals = y_test - y_pred
    ax2.scatter(y_pred, residuals, alpha=0.5)
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=2)
    ax2.set_xlabel('Predicted Values')
    ax2.set_ylabel('Residuals')
    ax2.set_title('Residual Plot')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = 'demo_results.png'
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    print(f"   Saved visualization to: {output_path}")
    plt.close()
    print()
    
    # 6. Summary
    print("=" * 60)
    print("✅ All dependencies validated successfully!")
    print("=" * 60)
    print()
    print("Library Versions:")
    print(f"   NumPy: {np.__version__}")
    print(f"   Pandas: {pd.__version__}")
    print(f"   Matplotlib: {plt.matplotlib.__version__}")
    print(f"   Scikit-Learn: {__import__('sklearn').__version__}")
    import scipy
    print(f"   SciPy: {scipy.__version__}")
    print()


if __name__ == "__main__":
    main()
