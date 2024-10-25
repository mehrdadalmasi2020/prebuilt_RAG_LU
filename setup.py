from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prebuilt_RAG_LU",  # New library name
    version="1.0.3",  # release version for the RAG-based system
    author="Mehrdad ALMASI, Demival VASQUES FILHO",
    author_email="mehrdad.al.2023@gmail.com, demival.vasques@uni.lu",
    description="A library for building Retrieval-Augmented Generation (RAG) systems using ChromaDB and popular language models (LLMs).",  
    long_description=long_description,  # Load detailed description from README
    long_description_content_type="text/markdown",  # README format
    url="https://github.com/mehrdadalmasi2020/prebuilt_RAG_LU",  # GitHub repository URL
    packages=find_packages(),  # Automatically find and include all packages
    include_package_data=True,  # Include additional non-Python files specified in MANIFEST.in
    install_requires=[  # Required dependencies for this project
        "transformers>=4.20.0,<5.0.0",  # Hugging Face Transformers, for LLMs like GPT, T5, and Mistral
        "torch>=1.7.0,<2.0.0",  # PyTorch for model usage
        "chromadb>=0.3.0",  # Chroma for vector database management
        "pandas>=1.1.0",  # For data manipulation
        "scikit-learn>=1.0",  # For dataset handling and evaluation
        "numpy>=1.19.0,<1.24.0",  # For numerical computations
        "openpyxl>=3.0.0",  # For handling Excel files, if needed
    ],
    classifiers=[  # Classifiers help users find your project by defining its audience, environment, and license
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",  # Indicating the library is in the beta stage
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",  # Ensuring compatibility with Python 3.6 and above
    keywords="RAG, Retrieval-Augmented Generation, transformers, ChromaDB, fine-tuning",  # Keywords for searchability
    project_urls={  # Additional links that are useful for the users of your library
        "Documentation": "https://github.com/mehrdadalmasi2020/prebuilt_RAG_LU",
        "Source": "https://github.com/mehrdadalmasi2020/prebuilt_RAG_LU",
        "Tracker": "https://github.com/mehrdadalmasi2020/prebuilt_RAG_LU/issues",
    },
)
