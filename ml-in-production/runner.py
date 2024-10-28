from model_service import ModelService

def main():
    model_service = ModelService()
    model_service.load_model()
    predictions = model_service.predict([85, 2015, 2, 20, 1, 1, 0, 0, 1])
    print(predictions)

if __name__ == '__main__':
    main()