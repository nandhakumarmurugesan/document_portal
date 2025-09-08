import os
import fitz  #required to work with pyPDFwhat br
import uuid
from datetime import datetime
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentHandler:
    """"
    Handles PDF saving and reading operations
    Automatically logs all actions and supports session-based organizations
    """
    def __init__(self,data_dir=None,session_id=None):
        #session history for every instance
        try:
            self.log = CustomLogger().get_logger(__name__)
            #check data directory from env variable or use default path
            self.data_dir = data_dir or os.getenv(
                                    "DATA_STORAGE_PATH",
                                    os.path.join(os.getcwd(),"data","document_analysis") 
            )
            self.session_id = session_id or f"session_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}" 
            
            #create base session directory
            self.session_path = os.path.join(self.data_dir,self.session_id)
            os.makedirs(self.session_path,exist_ok=True) 
            
            self.log.info("PDFHandler initialized", session_id=self.session_id, session_path=self.session_path)
        
        except Exception as e:        
            self.log.error(f"Error during PDFHandler initialization: {e}")
            raise DocumentPortalException("Error initializing DocumentHadler", e) from e
    
    def save_pdf():
        try:
            pass
        except Exception as e:        
            self.log.error(f"Error during saving PDF: {e}")
            raise DocumentPortalException("Error saving PDF", e) from e
    
    def read_pdf():
        try:
            pass
        except Exception as e:
            self.log.error(f"Error during reading PDF: {e}")
            raise DocumentPortalException("Error reading PDF", e) from e
        
if __name__ == "__main__":
    handler = DocumentHandler()
    print(f"Session ID: {handler.session_id}")
    print(f"Session Path: {handler.session_path}")
    #handler.save_pdf()
    #handler.read_pdf()