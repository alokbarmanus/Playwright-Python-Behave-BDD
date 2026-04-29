import os
import json

class DataUtil:
        @staticmethod
        def get_scenario_data(context):
            """
            Returns data from the file specified in the @dataFile tag for the scenario.
            Raises an error if @dataFile is missing.
            """
            data_file = None
            for tag in getattr(context.scenario, 'effective_tags', []):
                if tag.startswith('dataFile:'):
                    data_file = tag.split(':', 1)[1]
                    env = os.environ.get('ENV', 'dev').lower()
                    data_file = data_file.replace('${env}', env)
                    break
            if not data_file:
                raise ValueError("@dataFile tag is required in the scenario for dynamic data loading.")
            filename = os.path.basename(data_file)
            data = DataUtil.get_json_data(filename)
            if isinstance(data, list):
                data = data[0]
            return data

        @staticmethod
        def get_json_data(filename, env=None):
            """
            Reads a JSON file from the data/{env}/ directory.
            :param filename: Name of the JSON file (e.g., 'registrationData.json')
            :param env: Environment name (default: from ENV variable or 'dev')
            :return: Parsed JSON data
            """
            if env is None:
                env = os.environ.get('ENV', 'dev').lower()
            data_path = os.path.join('data', env, filename)
            with open(data_path, 'r') as f:
                data = json.load(f)
            return data

        @staticmethod
        def get_login_data(env=None):
            return DataUtil.get_json_data('loginData.json', env)
