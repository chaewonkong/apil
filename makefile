GREEN=\n\033[1;32;40m
RED=\n\033[1;31;40m
NC=\033[0m # No Color

run:
	@/bin/sh -c "echo \"${GREEN}[App 시작]${NC}\""
	pipenv run uvicorn main:app --reload --port 5000
