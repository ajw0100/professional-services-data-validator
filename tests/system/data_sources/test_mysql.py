# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from data_validation import data_validation, consts, exceptions
from data_validation.query_builder import query_builder


# TODO: To use this code I would need to whitelist the MySQL instance
MYSQL_CONFIG_INVALID = {
    # Configuration Required for All Data Soures
    "source_type": "MySQL",
    # BigQuery Specific Connection Config
    "config": {
        "host": "35.227.139.75",
        "user": "root",
        "password": "password",
        "port": 3306,
        "database": "guestbook",
        "driver": "pymysql",
    },
    # Configuration Required Depending on Validator Type
    "schema_name": "guestbook",
    "table_name": "entries",
    consts.PARTITION_COLUMN: "starttime",
}


def test_mysql_count_invalid_host():
    throws_error = False
    builder = query_builder.QueryBuilder.build_count_validator()
    try:
        data_validator = data_validation.DataValidation(
            builder,
            MYSQL_CONFIG_INVALID,
            MYSQL_CONFIG_INVALID,
            result_handler=None,
            verbose=False,
        )
        df = data_validator.execute()
    except exceptions.DataClientConnectionFailure:
        throws_error = True