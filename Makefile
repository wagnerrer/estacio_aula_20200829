PROJECT_NAME := aula_20200829
PYTHON_VERSION := 3.6.9
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

.pip:
	pip install pip==20.2.2

setup: .pip
	pip install -r requirements.txt

.create-venv:
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup