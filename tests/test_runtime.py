"""
Test Runtime - Analytics Service Backend
Tests for core dependency functionality and compatibility
"""

import pytest
import sys


class TestDependencyImports:
    """Test that all critical dependencies can be imported successfully."""
    
    def test_import_numpy(self):
        """Verify numpy is properly installed and importable."""
        import numpy as np
        assert np.__version__
        print(f"✓ numpy version: {np.__version__}")
    
    def test_import_pandas(self):
        """Verify pandas is properly installed and importable."""
        import pandas as pd
        assert pd.__version__
        print(f"✓ pandas version: {pd.__version__}")
    

    def test_import_scipy(self):
        """Verify scipy is properly installed and importable."""
        import scipy
        assert scipy.__version__
        print(f"✓ scipy version: {scipy.__version__}")
    
    def test_import_matplotlib(self):
        """Verify matplotlib is properly installed and importable."""
        import matplotlib
        assert matplotlib.__version__
        print(f"✓ matplotlib version: {matplotlib.__version__}")
    
    def test_import_fastapi(self):
        """Verify fastapi is properly installed and importable."""
        import fastapi
        assert fastapi.__version__
        print(f"✓ fastapi version: {fastapi.__version__}")
    
    def test_import_uvicorn(self):
        """Verify uvicorn is properly installed and importable."""
        import uvicorn
        assert uvicorn.__version__
        print(f"✓ uvicorn version: {uvicorn.__version__}")


class TestNumpyFunctionality:
    """Test basic numpy operations."""
    
    def test_numpy_array_creation(self):
        """Test basic numpy array creation."""
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        assert len(arr) == 5
        assert arr.dtype == np.int64 or arr.dtype == np.int32
    
    def test_numpy_arithmetic(self):
        """Test numpy arithmetic operations."""
        import numpy as np
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        result = arr1 + arr2
        assert np.array_equal(result, np.array([5, 7, 9]))
    
    def test_numpy_statistics(self):
        """Test numpy statistics functions."""
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        assert np.mean(arr) == 3.0
        assert np.std(arr) > 0


class TestPandasFunctionality:
    """Test basic pandas operations."""
    
    def test_pandas_dataframe_creation(self):
        """Test pandas DataFrame creation."""
        import pandas as pd
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        assert df.shape == (3, 2)
    
    def test_pandas_series_creation(self):
        """Test pandas Series creation."""
        import pandas as pd
        series = pd.Series([10, 20, 30, 40])
        assert len(series) == 4
        assert series.mean() == 25.0
    
    def test_pandas_dataframe_operations(self):
        """Test basic pandas DataFrame operations."""
        import pandas as pd
        df = pd.DataFrame({'X': [1, 2, 3], 'Y': [10, 20, 30]})
        assert df['X'].sum() == 6
        assert df['Y'].mean() == 20.0


class TestScipyFunctionality:
    """Test basic scipy operations."""
    
    def test_scipy_import_submodules(self):
        """Test scipy submodule imports."""
        from scipy import stats
        from scipy import optimize
        assert stats
        assert optimize
    
    def test_scipy_statistical_functions(self):
        """Test scipy statistical functions."""
        from scipy import stats
        import numpy as np
        
        data = np.array([1, 2, 3, 4, 5])
        mean_val = np.mean(data)
        assert mean_val == 3.0


class TestMatplotlibFunctionality:
    """Test basic matplotlib operations."""
    
    def test_matplotlib_import_pyplot(self):
        """Test matplotlib pyplot import."""
        import matplotlib.pyplot as plt
        assert plt
    
    def test_matplotlib_figure_creation(self):
        """Test matplotlib figure creation."""
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 2, 3])
        assert fig is not None


class TestFastAPIFunctionality:
    """Test basic FastAPI functionality."""
    
    def test_fastapi_app_creation(self):
        """Test FastAPI app creation."""
        from fastapi import FastAPI
        app = FastAPI()
        assert app is not None
        assert hasattr(app, 'get')
        assert hasattr(app, 'post')
    
    def test_fastapi_route_definition(self):
        """Test FastAPI route definition."""
        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/health")
        def health_check():
            return {"status": "ok"}
        
        # Check route was registered
        assert len(app.routes) > 0


class TestUvicornImport:
    """Test uvicorn basic functionality."""
    
    def test_uvicorn_config_creation(self):
        """Test uvicorn Config object creation."""
        from fastapi import FastAPI
        from uvicorn import Config
        
        app = FastAPI()
        config = Config(app=app, host="127.0.0.1", port=8000)
        assert config is not None


class TestPythonVersion:
    """Test Python version compatibility."""
    
    def test_python_version_requirement(self):
        """Test that Python 3.10+ is being used."""
        major, minor = sys.version_info.major, sys.version_info.minor
        assert major >= 3, f"Python 3+ required, got {major}.{minor}"
        assert major >= 4 or (major == 3 and minor >= 10), \
            f"Python 3.10+ required, got {major}.{minor}"


# Test configuration
if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
