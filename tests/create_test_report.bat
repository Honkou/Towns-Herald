@echo off
coverage run

coverage report
coverage lcov
coverage html
