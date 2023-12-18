# import quickfix as fix

# class MyApplication(fix.Application):
#     def onCreate(self, sessionID: fix.SessionID):
#         print("Соединение установлено успешно.")

#     def onLogon(self, sessionID: fix.SessionID):
#         print("Успешный вход в систему.")
        
#     def onLogout(self, sessionID: fix.SessionID):
#         print("Выход из системы.")

#     def toAdmin(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def fromAdmin(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def toApp(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def fromApp(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

# def main():
#     initiator = None  # Инициализация переменной initiator
#     try:
#         settings = fix.SessionSettings(r"D:\Проекты VS code\FIX протокл (работа)\connecter.cfg")  # Замените на путь к вашему конфигурационному файлу FIX
#         application = MyApplication()
#         storeFactory = fix.FileStoreFactory(settings)
#         logFactory = fix.FileLogFactory(settings)
#         initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
#         initiator.start()

#         while True:
#             pass  # Запуск приложения, ожидание событий

#     except fix.ConfigError as e:
#         print("Ошибка конфигурации:", e)
#     except fix.RuntimeError as e:
#         print("Ошибка запуска:", e)
#     finally:
#         if initiator is not None:
#             initiator.stop()

# if __name__ == "__main__":
#     main()


# import quickfix as fix

# class MyApplication(fix.Application):
#     def onCreate(self, sessionID: fix.SessionID):
#         print("Соединение установлено успешно.")

#     def onLogon(self, sessionID: fix.SessionID):
#         print("Успешный вход в систему.")

#         # Отправляем запрос на получение котировки EUR/USD при успешном входе в систему
#         marketDataRequest = self.createMarketDataRequest()
#         fix.Session.sendToTarget(marketDataRequest, sessionID)

#     def onLogout(self, sessionID: fix.SessionID):
#         print("Выход из системы.")

#     def toAdmin(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def fromAdmin(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def toApp(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def fromApp(self, message, sessionID):
#         if message.getHeader().getField(fix.MsgType()) == fix.MsgType_MarketDataSnapshotFullRefresh:
#             symbol = fix.Symbol()
#             message.getField(symbol)

#             if symbol.getValue() == "EUR/USD":
#                 noEntries = fix.NoMDEntries()
#                 message.getField(noEntries)

#                 for i in range(1, noEntries.getValue() + 1):
#                     entryType = fix.MDEntryType()
#                     message.getField(entryType, i)

#                     if entryType.getValue() == fix.MDEntryType_BID or entryType.getValue() == fix.MDEntryType_OFFER:
#                         price = fix.MDEntryPx()
#                         message.getField(price, i)

#                         print(f"EUR/USD {entryType.getValue()}: {price.getValue()}")

#     def createMarketDataRequest(self):
#         marketDataRequest = fix.Message()
#         header = marketDataRequest.getHeader()

#         header.setField(fix.MsgType(fix.MsgType_MarketDataRequest))
#         header.setField(fix.SenderCompID("MARKET_1675_1"))
#         header.setField(fix.TargetCompID("UNITY_RU_PROD"))
#         header.setField(fix.MsgSeqNum(fix.SeqNum()))

#         marketDataRequest.setField(fix.SubscriptionRequestType(fix.SubscriptionRequestType_SNAPSHOT))
#         marketDataRequest.setField(fix.MarketDepth(0))
#         marketDataRequest.setField(fix.Symbol("EUR/USD"))
#         marketDataRequest.setField(fix.NoMDEntryTypes(2))
#         marketDataRequest.setField(fix.MDEntryType(0, fix.MDEntryType_BID))
#         marketDataRequest.setField(fix.MDEntryType(1, fix.MDEntryType_OFFER))

#         return marketDataRequest

# def main():
#     initiator = None
#     try:
#         settings = fix.SessionSettings(r"D:\Проекты VS code\FIX протокл (работа)\connecter.cfg")
#         application = MyApplication()
#         storeFactory = fix.FileStoreFactory(settings)
#         logFactory = fix.FileLogFactory(settings)
#         initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
#         initiator.start()

#         while True:
#             pass  # Ожидание событий

#     except fix.ConfigError as e:
#         print("Ошибка конфигурации:", e)
#     except fix.RuntimeError as e:
#         print("Ошибка запуска:", e)
#     finally:
#         if initiator is not None:
#             initiator.stop()

# if __name__ == "__main__":
#     main()

# import quickfix as fix

# class MyApplication(fix.Application):
#     def onCreate(self, sessionID: fix.SessionID):
#         print("Соединение установлено успешно.")

#     def onLogon(self, sessionID: fix.SessionID):
#         print("Успешный вход в систему.")
        
#     def onLogout(self, sessionID: fix.SessionID):
#         print("Выход из системы.")

#     def toAdmin(self, message: fix.Message, sessionID: fix.SessionID):
#         # Проверяем, что тип сообщения - Logon (35=A)
#         if message.getHeader().getField(fix.MsgType()) == fix.MsgType_Logon:
#             # Создаем сообщение для входа в систему (Logon)
#             logon_message = fix.Message()
#             header = logon_message.getHeader()
#             header.setField(fix.MsgType(fix.MsgType_Logon))  # Устанавливаем тип сообщения Logon (35=A)
#             # Можно добавить другие поля, если необходимо, например, учетные данные

#             # Отправляем сообщение
#             session = fix.Session.lookupSession(sessionID)
#             if session:
#                 session.send(logon_message)
#             else:
#                 print("Ошибка: Не удалось найти сессию для отправки сообщения Logon.")

#     def fromAdmin(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def toApp(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

#     def fromApp(self, message: fix.Message, sessionID: fix.SessionID):
#         pass

# # Остальная часть вашего кода остается неизменной

# def main():
#     initiator = None  # Инициализация переменной initiator
#     try:
#         settings = fix.SessionSettings(r"D:\Проекты VS code\FIX протокл (работа)\connecter.cfg")  # Замените на путь к вашему конфигурационному файлу FIX
#         application = MyApplication()
#         storeFactory = fix.FileStoreFactory(settings)
#         logFactory = fix.FileLogFactory(settings)
#         initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
#         initiator.start()

#         while True:
#             pass  # Запуск приложения, ожидание событий

#     except fix.ConfigError as e:
#         print("Ошибка конфигурации:", e)
#     except fix.RuntimeError as e:
#         print("Ошибка запуска:", e)
#     finally:
#         if initiator is not None:
#             initiator.stop()

# if __name__ == "__main__":
#     main()


import quickfix as fix

class MyApplication(fix.Application):
    def onCreate(self, sessionID: fix.SessionID):
        print("Соединение установлено успешно.")

    def onLogon(self, sessionID: fix.SessionID):
        print("Успешный вход в систему.")
        self.sendMarketDataRequest(sessionID)  # Отправляем запрос на маркет-дату после входа в систему

    def onLogout(self, sessionID: fix.SessionID):
        print("Выход из системы.")

    def sendMarketDataRequest(self, sessionID: fix.SessionID):
        marketDataRequest = fix.Message()

        header = marketDataRequest.getHeader()
        header.setField(fix.MsgType(fix.MsgType_MarketDataRequest))
        header.setField(fix.SenderCompID("MARKET_1675_1"))  # Укажите ваш SenderCompID
        header.setField(fix.TargetCompID("UNITY_RU_PROD"))  # Укажите TargetCompID вашего брокера
        header.setField(fix.BeginString("FIX.4.4"))

        marketDataRequest.setField(fix.MDReqID("MarketDataRequestID"))  # Уникальный идентификатор запроса
        marketDataRequest.setField(fix.SubscriptionRequestType(fix.SubscriptionRequestType_SNAPSHOT_PLUS_UPDATES))
        marketDataRequest.setField(fix.MarketDepth(0))  # Тип данных запроса (0 - запрос Snapshot)
        marketDataRequest.setField(fix.NoRelatedSym(1))  # Количество инструментов в запросе
        marketDataRequest.setField(fix.Symbol("EUR/USD"))  # Символ (например, валютная пара)

        fix.Session.sendToTarget(marketDataRequest, sessionID)

    def toAdmin(self, message, sessionID):
        # Логика для обработки и/или изменения исходящих сообщений перед их отправкой
        # Например, добавление необходимых данных в заголовок сообщения
        print(message)
        pass

    def fromAdmin(self, message, sessionID):
        # Логика для обработки входящих сообщений до их обработки библиотекой QuickFIX
        print(message)
        pass

    def toApp(self, message, sessionID):
        # Логика для обработки и/или изменения исходящих приложением сообщений перед их отправкой
        print(message)
        pass


    def fromApp(self, message, sessionID):
        try:
            if message.getHeader().getField(fix.MsgType()) == fix.MsgType_MarketDataSnapshotFullRefresh:
                # Получение рыночных данных
                symbol = message.getField(fix.Symbol())
                # Обработка полученных данных
                print("Получены рыночные данные для", symbol)
        except fix.FieldNotFound:
            pass

# Остальная часть вашего кода остается неизменной

def main():
    initiator = None
    try:
        settings = fix.SessionSettings(r"D:\Проекты VS code\FIX протокл (работа)\connecter.cfg")  # Укажите путь к вашему конфигурационному файлу FIX
        application = MyApplication()
        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
        initiator.start()

        while True:
            pass  # Цикл ожидания событий

    except fix.ConfigError as e:
        print("Ошибка конфигурации:", e)
    except fix.RuntimeError as e:
        print("Ошибка запуска:", e)
    finally:
        if initiator is not None:
            initiator.stop()

if __name__ == "__main__":
    main()
