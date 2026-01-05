"""
test_runtime.py - Runtime validation tests for upgraded dependencies

Tests core functionality of all major dependencies to ensure:
1. Packages are installed correctly
2. Basic operations work as expected
3. No breaking changes affect common use cases
"""

import pytest
import sys


class TestPythonEnvironment:
    """Test Python environment compatibility"""
    
    def test_python_version(self):
        """Verify Python 3.10+ is being used"""
        assert sys.version_info >= (3, 10), f"Python 3.10+ required, got {sys.version_info}"


class TestNumpy:
    """Test numpy core functionality"""
    
    def test_numpy_import(self):
        """Test numpy can be imported"""
        import numpy as np
        assert np.__version__ >= "1.26.0"
    
    def test_numpy_array_operations(self):
        """Test basic numpy array operations"""
        import numpy as np
        
        arr = np.array([1, 2, 3, 4, 5])
        assert arr.sum() == 15
        assert arr.mean() == 3.0
        assert arr.std() > 0
    
    def test_numpy_matrix_operations(self):
        """Test numpy matrix operations"""
        import numpy as np
        
        matrix_a = np.array([[1, 2], [3, 4]])
        matrix_b = np.array([[5, 6], [7, 8]])
        result = np.dot(matrix_a, matrix_b)
        
        expected = np.array([[19, 22], [43, 50]])
        assert np.array_equal(result, expected)


class TestPandas:
    """Test pandas core functionality"""
    
    def test_pandas_import(self):
        """Test pandas can be imported"""
        import pandas as pd
        assert pd.__version__ >= "2.2.0"
    
    def test_dataframe_creation(self):
        """Test DataFrame creation and basic operations"""
        import pandas as pd
        
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': ['a', 'b', 'c', 'd', 'e']
        })
        
        assert len(df) == 5
        assert df['A'].sum() == 15
        assert df['B'].mean() == 30.0
    
    def test_dataframe_operations(self):
        """Test pandas data manipulation"""
        import pandas as pd
        
        df = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [2, 4, 6, 8, 10]
        })
        
        df['z'] = df['x'] + df['y']
        assert df['z'].tolist() == [3, 6, 9, 12, 15]


class TestScikitLearn:
    """Test scikit-learn core functionality"""
    
    def test_sklearn_import(self):
        """Test scikit-learn can be imported"""
        import sklearn
        assert sklearn.__version__ >= "1.5.0"
    
    def test_linear_regression(self):
        """Test basic linear regression"""
        from sklearn.linear_model import LinearRegression
        import numpy as np
        
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10])
        
        model = LinearRegression()
        model.fit(X, y)
        
        predictions = model.predict([[6]])
        assert abs(predictions[0] - 12) < 0.1
    
    def test_train_test_split(self):
        """Test train/test split functionality"""
        from sklearn.model_selection import train_test_split
        import numpy as np
        
        X = np.arange(100).reshape((100, 1))
        y = np.arange(100)
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        assert len(X_train) == 80
        assert len(X_test) == 20


class TestMatplotlib:
    """Test matplotlib core functionality"""
    
    def test_matplotlib_import(self):
        """Test matplotlib can be imported"""
        import matplotlib
        assert matplotlib.__version__ >= "3.9.0"
    
    def test_plot_creation(self):
        """Test basic plot creation"""
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Test Plot")
        
        assert ax.get_title() == "Test Plot"
        plt.close(fig)


class TestScipy:
    """Test scipy core functionality"""
    
    def test_scipy_import(self):
        """Test scipy can be imported"""
        import scipy
        assert scipy.__version__ >= "1.14.0"
    
    def test_scipy_stats(self):
        """Test scipy statistics functions"""
        from scipy import stats
        import numpy as np
        
        data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        
        assert abs(mean - 5.5) < 0.01
        assert std > 0
    
    def test_scipy_optimization(self):
        """Test scipy optimization"""
        from scipy.optimize import minimize
        
        # Minimize (x-2)^2
        result = minimize(lambda x: (x - 2)**2, x0=0)
        assert abs(result.x[0] - 2.0) < 0.01


class TestFastAPI:
    """Test FastAPI core functionality"""
    
    def test_fastapi_import(self):
        """Test FastAPI can be imported"""
        import fastapi
        assert fastapi.__version__ >= "0.115.0"
    
    def test_fastapi_app_creation(self):
        """Test FastAPI app instantiation"""
        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/")
        async def root():
            return {"message": "Hello World"}
        
        assert app is not None
        assert len(app.routes) > 0


class TestUvicorn:
    """Test uvicorn core functionality"""
    
    def test_uvicorn_import(self):
        """Test uvicorn can be imported"""
        import uvicorn
        assert uvicorn.__version__ >= "0.32.0"


class TestPytest:
    """Test pytest itself"""
    
    def test_pytest_version(self):
        """Test pytest version"""
        import pytest
        assert pytest.__version__ >= "8.3.0"


class TestIntegration:
    """Integration tests combining multiple libraries"""
    
    def test_sklearn_pandas_integration(self):
        """Test scikit-learn with pandas DataFrames"""
        import pandas as pd
        from sklearn.linear_model import LogisticRegression
        import numpy as np
        
        # Create sample data
        df = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5, 6, 7, 8],
            'feature2': [2, 3, 4, 5, 6, 7, 8, 9],
            'target': [0, 0, 0, 0, 1, 1, 1, 1]
        })
        
        X = df[['feature1', 'feature2']]
        y = df['target']
        
        model = LogisticRegression()
        model.fit(X, y)
        
        predictions = model.predict(X)
        assert len(predictions) == len(y)
    
    def test_numpy_pandas_matplotlib_pipeline(self):
        """Test data pipeline with numpy, pandas, and matplotlib"""
        import numpy as np
        import pandas as pd
        import matplotlib
        matplotlib.use('Agg')  # Use non-GUI backend
        import matplotlib.pyplot as plt
        
        # Generate data with numpy
        x = np.linspace(0, 10, 50)
        y = 2 * x + np.random.normal(0, 1, 50)
        
        # Process with pandas
        df = pd.DataFrame({'x': x, 'y': y})
        df['y_smooth'] = df['y'].rolling(window=5, center=True).mean()
        
        # Plot with matplotlib
        fig, ax = plt.subplots()
        ax.scatter(df['x'], df['y'], alpha=0.5, label='Raw')
        ax.plot(df['x'], df['y_smooth'], 'r-', label='Smoothed')
        ax.legend()
        
        assert len(df) == 50
        plt.close(fig)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
