#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { CdkLambdaFastapiStack } from "../lib/lambda-fastapi";

const app = new cdk.App();
new CdkLambdaFastapiStack(app, "CdkLambdaFastapiStack", {});