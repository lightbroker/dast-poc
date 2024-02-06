TIMESTAMP=$(date +%s)
TARGET='altoro.testfire.net'
mkdir -p .zap/reports/
cat report_md.md > ".zap/reports/dast_$TARGET_$TIMESTAMP.md"
cat report_json.json | jq > ".zap/reports/dast_$TARGET_$TIMESTAMP.json"
rm report_*
git config user.name github-actions
git config user.email github-actions@github.com
git add .
git commit -m "report output: $TIMESTAMP"
git push