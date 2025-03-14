from Перевод import ПочтовыйПеревод, БанковскийПеревод, ВалютныйПеревод

почтовый: ПочтовыйПеревод = ПочтовыйПеревод(1000, "Иванов И.И.", "12345")
почтовый.выполнить()

банковский: БанковскийПеревод = БанковскийПеревод(2000,
                                                  "Петров П.П.", "Сбербанк")
банковский.выполнить()

валютный: ВалютныйПеревод = ВалютныйПеревод(1500,
                                            "Сидоров С.С.", "Тинькофф", "USD")
валютный.выполнить()

# Пример выполнения программы:
# Выполняется почтовый перевод на сумму 1000 к
# получателю Иванов И.И.. Номер передачи: 12345.
# Выполняется банковский перевод на сумму 2000 к
# получателю Петров П.П.. Банк: Сбербанк.
# Выполняется валютный перевод на сумму 1500 USD к
# получателю Сидоров С.С.. Банк: Тинькофф.
