#!/bin/bash
twine upload --skip-existing  -p "${TWINE_LIVE_TOKEN}" dist/*
