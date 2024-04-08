import os
import sys

my_path = os.getcwd()


def color_text(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"


def check_pom_exist():
    # This function checks if the pom file does exist to decide whether it create it or not
    file = my_path + "\pom.xml"
    return os.path.isfile(file)


def create_pom(project_name):
    if not check_pom_exist():
        with open("pom.xml", "w") as file:
            file.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>za.co.wethinkcode</groupId>
    <artifactId>{project_name}</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

    <dependencies>                                              
        <dependency>                                            
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.2</version>
            <scope>test</scope>                                 
        </dependency>
    </dependencies>
</project>''')
    else:
        print("pom file already exists...")


def main():
    arg = sys.argv
    if len(arg) == 1:
        print(color_text("Please pass project name to create pom file.", "red"))
    elif arg[1] == "-p" and len(arg) == 3:
        create_pom(arg[2])
        print(color_text("pom file created successfully...", "green"))

    else:
        print(color_text("format:  pom -p project_name", 'red'))


if __name__ == '__main__':
    main()
