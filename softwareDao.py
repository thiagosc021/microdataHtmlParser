import os
import sqlite3
from software import Software, Screenshot, Link, Image,Review
 
class DataAccessor(object):
    '''
    Classe que gerencia o acesso ao banco de dados
    '''
    def __init__(self, dbpath):
        if os.path.exists(dbpath):
            self.conn = sqlite3.connect(dbpath)
            self.conn.text_factory = str
            self.conn.row_factory = sqlite3.Row
        else:
            print "Banco de dados nao encontrado: ", dbpath
        
 
    def readSoftware(self, id):
        '''
        retorna o software pelo id
        carrega todos os relacionamento do software
            software_screenshot
            software_link
            software_image
            software_review
        '''
        software=None
        try:
            self.cur = self.conn.cursor()
            stmt = 'SELECT *'
            stmt += "\nFROM software_software" 
            stmt += "\nWHERE id=?"
            stmt += ';'
            self.cur.execute(stmt,[id])
            data = self.cur.fetchone()
            if data:
              software= Software(data["id"],data["name"],data["text"],data["downloadUrl"],data["applicationSubCategory"])
              
            stmt = 'select * from software_screenshot where software_id=?'
            self.cur.execute(stmt,[id])
            rows = self.cur.fetchall()
            for row in rows:
              software.screenshotList.append(Screenshot(row["url_screenshot"]))

            stmt = 'select * from software_link where software_id=?'
            self.cur.execute(stmt,[id])
            rows = self.cur.fetchall()
            for row in rows:
              software.linkList.append(Link(row["url_link"]))

            stmt = 'select * from software_image where software_id=?'
            self.cur.execute(stmt,[id])
            rows = self.cur.fetchall()
            for row in rows:
              software.imageList.append(Image(row["url_image"]))

            stmt = 'select * from software_review where software_id=?'
            self.cur.execute(stmt,[id])
            data = self.cur.fetchone()
            if data:
              software.review = Review(data["reviewBody"],data["ratingValue"])


            return software
        finally:
            self.cur.close()

    def includeSoftware(self,software):
        try:
            self.cur = self.conn.cursor()
            stmtInsert = "INSERT INTO software_software VALUES (?,?,?,?,?)"
            self.cur.execute(stmtInsert,[software.id,str(software.name), software.text.encode('utf-8'), str(software.downloadUrl), str(software.applicationSubCategory)])
            
            images = []
            i=1
            for image in software.imageList :
               images.append((i,1, str(image.url_image)))
               i=i+1

            self.cur.executemany("INSERT INTO software_image VALUES (?,?,?)", images)
            
            links = []
            i=1
            for link in software.linkList :
               links.append((i,1, str(link.url_link)))
               i=i+1

            self.cur.executemany("INSERT INTO software_link VALUES (?,?,?)", links)

            screenshots = []
            i=1
            for screenshot in software.screenshotList :
               screenshots.append((i,1, str(screenshot.url_screenshot)))
               i=i+1

            self.cur.executemany("INSERT INTO software_screenshot VALUES (?,?,?)", screenshots)
            
            review = [1,1,software.review.reviewBody.encode('utf-8'),software.review.ratingValue]
            self.cur.execute("INSERT INTO software_review VALUES (?,?,?,?)", review)

            self.conn.commit()
        finally:
            self.cur.close()

    def deleteSoftware(self,id_software):
        try:
            self.cur = self.conn.cursor()
            stmtDelete = "delete from software_software where id = ?"
            self.cur.execute(stmtDelete,[id_software])
            sql = "DELETE FROM software_screenshot where software_id=?"
            self.cur.execute(sql,[id_software])
            sql = "DELETE FROM software_link  where software_id=?"
            self.cur.execute(sql,[id_software])
            sql = "DELETE FROM software_image  where software_id=?"
            self.cur.execute(sql,[id_software])
            sql = "DELETE FROM software_review  where software_id=?"
            self.cur.execute(sql,[id_software])
            self.conn.commit()
        finally:
            self.cur.close()