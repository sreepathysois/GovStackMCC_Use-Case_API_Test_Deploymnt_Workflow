from fastapi import FastAPI, Form 

app = FastAPI()

@app.get("/home")
async def root():
     return {
  "message": "Welcome to Mother and Child Care Application", 
    "RequiredDocuments": 
       [ "UUID" ,"NID", "RationCard"] ,

  "EligibalityCriteria": ["PaySlip", "IncomeCertificate"]
  
  
} 

@app.post("/register_user/")
async def register(MotherName: str = Form(), NID_Mother: int  = Form(), BabyName: str = Form(), NID_Baby: int  = Form(),BirthLocation: str = Form(), BirthPlace: str = Form(), BirthTime: str = Form() ):
    return {"Registration_Token": 10,
            "Registration_Status": "Success"}

@app.get("/Digital_Registries_BB/{nid_citizen}")
async def citizen_details(nid_citizen: str):
    return {"ID": nid_citizen, 
             "FirstName" : "Smith Carry", 
             "LastName": " John Helmut", 
             "BirthCertificateID": "RR-123456789"}


@app.post("/RegistrationPayment/")
async def payment(Payment_Gateway: str = Form(), CardDetails: int  = Form(), CardHolderName: str = Form(), CVV: int  = Form(), RegistrationAmount: int = Form()):
    return {"Payment Status": "Sucess"}



@app.post("/GetConsent/")
async def consent(HealthCareWorkerName: str = Form(), HealthCareWorkerID: int  = Form(), MotherName: str = Form(), MotherNID: int  = Form()):
    return {"ConsentStatus": "Sucess",
           "Consent_Token" : "34567-88956" }
