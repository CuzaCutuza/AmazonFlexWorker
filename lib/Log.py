class Log:
    
    @staticmethod 
    def info(message: str):
        print(f'INFO: {message}', flush=True)

    @staticmethod
    def error(message: str):
        print(f'ERROR: {message}', flush=True)
    
    @staticmethod
    def offer(version: str, message: str):
        print(f'Version:{version}\nOffers:{message}\n', flush=True)
