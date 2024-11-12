#!/bin/bash
twine upload --skip-existing -u "${TWINE_LIVE_USERNAME}" -p "${TWINE_LIVE_PASSWORD}" dist/*
