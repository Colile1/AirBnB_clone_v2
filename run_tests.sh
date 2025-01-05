#!/bin/bash

# Function to run unit tests for file storage
run_file_storage_tests() {
    echo "Running unit tests for file storage..."
    python3 -m unittest discover tests 2>&1 | tee test_results.txt
    result=$(tail -n 1 test_results.txt)
    if [[ $result == "OK" ]]; then
        echo "All file storage tests passed!"
    else
        echo "Some file storage tests failed. Check test_results.txt for details."
        exit 1
    fi
}

# Function to run unit tests for database storage
run_db_storage_tests() {
    echo "Running unit tests for database storage..."
    export HBNB_ENV=test
    export HBNB_MYSQL_USER=hbnb_test
    export HBNB_MYSQL_PWD=hbnb_test_pwd
    export HBNB_MYSQL_HOST=localhost
    export HBNB_MYSQL_DB=hbnb_test_db
    export HBNB_TYPE_STORAGE=db

    python3 -m unittest discover tests 2>&1 | tee test_results_db.txt || echo "Database tests failed"
    result=$(tail -n 1 test_results_db.txt)
    if [[ $result == "OK" ]]; then
        echo "All database storage tests passed!"
    else
        echo "Some database storage tests failed. Check test_results_db.txt for details."
        exit 1
    fi
}

# Main script execution
echo "Starting unit tests..."

# Run file storage tests
run_file_storage_tests

# Run database storage tests
run_db_storage_tests

echo "All tests completed successfully!"
