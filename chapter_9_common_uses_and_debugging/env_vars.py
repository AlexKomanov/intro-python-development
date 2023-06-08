import os

java_home = os.getenv('JAVA_HOME')

os.environ["STAGE"] = "Production"

stage = os.environ["STAGE"].upper()
output = f"We are running in {stage}"

if stage.startswith('PROD'):
    output = "Danger!!! - " + output

print(f"JAVA_HOME: {java_home}")
print(output)

