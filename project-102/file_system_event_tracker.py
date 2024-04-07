import sys
import random
import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\PRACHI\Desktop\Doc(102)"

class FileEventHandler(FileSystemEventHandler):
   def on_created(self,event):
      print(f"Hey,{event.src_path} has been created")

   def on_deleted(self,event):
       print(f"Oops someone deleted {event.src_path}")

   def on_modified(self,event):
       print(f"Hey there,{event.src_path} has been modified")

   def on_moved(self,event):
       print(f"Someone moved {event.src_path} to {event.des_path}")

       event_handler = FileEventHandler()
       observer = Observer()
       observer.shedule(event_handler,from_dir,recursive=True) 

       observer.start()

   try:
       while True:
           time.sleep(2)
           print("running...")

   except KeyboardInterrupt:
       print("stopped!")
       observer.stop()
              
                   