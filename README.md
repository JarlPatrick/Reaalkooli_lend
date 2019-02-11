# Reaalkooli_lend

Raspberry PI käivitamisel käivitub programm forever.py.
See kood käivitab programmi test.py ja kui test.py peaks lõppetama töötamise siis taaskäivitab selle.
See kood lisati sest testimisel test.py lõpetas millegipärast pärast pikka aega töötamise. Lennu ajal seda ei juhtunud.

test.py on põhikood mis mõõdab andmeid, teeb logi, saadab raadiosignaali ja avab ventilaatori klappid.
See kood erineb juhendis olevast ja on pytrack.tracker'i natuke muudetud kood.
See andis võimaluse teha logi otse koodi siseselt ja saada koodi siseselt hetke kõrgust teada mis oli vajalik klappide avamiseks.
Sensor kasutab koodi bme280.py. Tegemist pole koolitusel antud sensoriga kuna ei saanud seda tööle ja siis tellisin ise bme280 sensori.
tracker.py'd lennul ei kasutanud.
