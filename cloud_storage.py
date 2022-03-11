import dropbox

class Transfer_data:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.BDb8FdekXHItgz9aQohrEtMCTQ8gHz0oDplILVbnpjoJ_2ock47caYcFa5amOwSWNjxymxtippuzs_oFG5_hCCyTOJWPt6NCbjBt80gEUgImZl9Z2F899Qe6kkcHlv7qCOq0YWaqM0Na"
    transfer_data=Transfer_data(access_token)
    file_from=input("Enter the file name which you want to transfer")
    file_to=input("Enter the file path where you want to upload in dropbox")
    transfer_data.upload_files(file_from,file_to)
    print("The file has been uploaded successfully")
main()