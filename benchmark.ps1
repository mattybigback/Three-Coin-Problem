Get-ChildItem . -Filter results.txt | Foreach-Object {
    Remove-Item $_;
}
Get-ChildItem . -Name -Filter *.py | Foreach-Object {
    python -m timeit -n 100 $(Get-Content $_) | Out-File -FilePath .\$_.result;
    echo "$_ - $(Get-Content -tail 1 .\$_.result)" | Out-File -Append -FilePath results.txt;
    Remove-Item .\$_.result;
}
Get-Content results.txt