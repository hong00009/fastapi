import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import { aws_lambda as lambda } from "aws-cdk-lib";
import * as path from "path";
import { Architecture } from "aws-cdk-lib/aws-lambda";
import * as dotenv from "dotenv";

dotenv.config({ path: path.join(__dirname, "../../python/app/.env") });

export class CdkLambdaFastapiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new lambda.DockerImageFunction(this, "LambdaFunction_1", {
      code: lambda.DockerImageCode.fromImageAsset(
        path.join(__dirname, "../../python"),
        {
          cmd: ["main.handler"],
        }
      ),
      architecture: Architecture.ARM_64,
      environment: {
        MYSQL_USER: process.env.MYSQL_USER || "",
        MYSQL_PWD: process.env.MYSQL_PWD || "",
        MYSQL_PORT: process.env.MYSQL_PORT || "",
        MYSQL_DB: process.env.MYSQL_DB || "",
      },
      timeout: cdk.Duration.seconds(900),
    });
  }
}