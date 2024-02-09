# Usage:
#
#   $ ./publish_reports.sh 'example.hostname.com' $(pwd)
#


# define vars
TIMESTAMP=$(TZ=UTC date +%s)
UTC_DAY=$(TZ=UTC date +%d)
UTC_MONTH_NUMERIC=$(TZ=UTC date +%m)
UTC_MONTH_ALPHA=$(TZ=UTC date +%b | tr '[:upper:]' '[:lower:]')
UTC_YEAR=$(TZ=UTC date +%Y)
TARGET=$1
DIR_PATH="reporting/output/${UTC_YEAR}/${UTC_MONTH_NUMERIC}_${UTC_MONTH_ALPHA}/${UTC_DAY}"
EXECUTION_CONTEXT=$2

# create timestamped report output files and clean up
mkdir -p ${DIR_PATH}
cat ${EXECUTION_CONTEXT}/report_md.md > ${DIR_PATH}/dast_${TARGET}_${TIMESTAMP}.md
cat ${EXECUTION_CONTEXT}/report_json.json | jq > ${DIR_PATH}/dast_${TARGET}_${TIMESTAMP}.json
rm ${EXECUTION_CONTEXT}/report_*

# stage, commit, and push to repo
git config user.name github-actions
git config user.email github-actions@github.com
git add .
git commit -m "report output: $TIMESTAMP"
git push
