#!/bin/bash
. /automation/automation_venvs/volte_automation_venv/bin/activate
export ORACLE_HOME=/orasrc/product/19.3
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
nohup python /automation/automation_projects/sas-automation --type="$1" --path="$2" &> /automation/automation_projects/sas-automation/nohup.out &