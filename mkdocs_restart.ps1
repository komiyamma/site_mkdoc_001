# MkDocsサーバーだけを安全にリスタートするPowerShellスクリプト
# 1. ポート6283を使っているpython.exeのPIDを取得
# 2. そのプロセスだけを強制終了
# 3. MkDocsサーバーを再起動

$port = 6283
$mkdocs_pid = (Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty OwningProcess)
if ($mkdocs_pid) {
	Write-Host "Killing python.exe (PID: $mkdocs_pid) on port $port..."
	Stop-Process -Id $mkdocs_pid -Force
	Start-Sleep -Seconds 1
}
Write-Host "Starting MkDocs server on port $port..."
Start-Process -NoNewWindow -FilePath "C:/usr/python/python.exe" -ArgumentList "-m mkdocs serve -a 127.0.0.1:$port"
