
import mysql
import mysql.connector
from datetime import date


con = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    passwd = "",
    database = "login"
)

# create a cursor
cursor = con.cursor()

# admin login function
def login(arg):
    try:
        cursor.execute('SELECT * FROM admin WHERE username = %s and Password = %s', arg)
        return cursor.fetchone()

    except:
        return False

def addclient(arg):
    # print(arg)
    try:
        cursor.execute('INSERT into client (name,Address,Contact) VALUES (%s,%s,%s)',arg)
        con.commit()
        return True

    except:
        return False

def selectClient(gup):
    try:
        # print("get",gup)
        cursor.execute('SELECT * FROM client WHERE id = %s',gup)
        return cursor.fetchall()     
    except:
        return False

def selectProduct(gup):
    try:
        # print("get",gup)
        # cursor.execute('SELECT * FROM product WHERE id = %s',gup)
        cursor.execute('SELECT subcategory.id, subcategory.name, product.name, product.Name, product.code, product.Cost, product.stock FROM product LEFT JOIN subcategory ON subcategory.id = product.subcatName WHERE product.id = %s', gup)
        return cursor.fetchone()     
    except:
        return False


def addProduct(arg):
    # print(arg)
    try:
        cursor.execute('INSERT into product (subcatName,Name,code,Cost,stock) VALUES (%s,%s,%s,%s,%s)',arg)
        con.commit()
        return True
    except:
        return False

def updateProduct(arg):
    
    try:
        print("get",arg)
        cursor.execute('update product SET subcatName = %s, Name=%s, code = %s, Cost=%s, stock=%s where id=%s',arg)
        con.commit()
        return True

    except:
        return False


def addbill(arg):
    print(arg)
    try:
        cursor.execute('INSERT into bill(clientID,productID,quantity,Per_PC_cost,totalAmount) VALUE(%s,%s,%s,%s,%s)',arg)
        con.commit()
        return True
    except:
        return False


def viewClient():
    try:
        cursor.execute('SELECT * FROM client order by id desc')
        return cursor.fetchall()
    except:
        return False

def viewBill():
    try:
        cursor.execute('SELECT bill.id,client.name,product.name,bill.dates,bill.quantity,bill.Per_PC_cost,bill.totalAmount FROM bill left join client on client.id=bill.clientID left join product on product.id=bill.productID order by bill.id desc')
        return cursor.fetchall()
    except:
        return False


def viewBillToday():
    
    try:
        cursor.execute('SELECT * FROM bill where date(dates) = %s', (date.today(), ))
        return cursor.fetchall()
    except:
        return False

def clientBillToday(name):
    
    try:
        cursor.execute('SELECT * FROM bill where date(dates) = %s and clientID = %s', (date.today(), name))
        return cursor.fetchall()
    except:
        return False

def dynamicClients():
    try:
        cursor.execute('SELECT id,Name FROM client')
        return cursor.fetchall()
    except:
        return False

def dynamicProduct():
    try:
        cursor.execute('SELECT id,Name FROM product')
        return cursor.fetchall()
    except:
        return False

def viewproduct():
    try:
        cursor.execute('SELECT * FROM product order by id desc')
        return cursor.fetchall()
    except:
        return False

def deleteclient(gup):
    try:
        print(gup)
        cursor.execute('DELETE FROM client WHERE id = %s',gup)
        con.commit()
        return True

    except:
        return False

def updateclient(gup):
    try:
        print("this",gup)
        cursor.execute('update client SET name=%s, Address=%s, Contact=%s where id=%s',gup)
        con.commit()
        # print(gup)
        return True

    except:
        return False


def deleteproduct(gup):
    try:
        print('delete',gup)
        cursor.execute('DELETE FROM product WHERE id = %s',gup)
        con.commit()
        return True

    except:
        return False



def singleBill(id):
    try:
        cursor.execute('SELECT bill.id,client.name,product.name,bill.dates,bill.quantity,bill.Per_PC_cost,bill.totalAmount FROM bill left join client on client.id=bill.clientID left join product on product.id=bill.productID where bill.id = %s', id)
        return cursor.fetchone()
    except: 
        return False



def clientBill(name):
    
    try:
        cursor.execute('SELECT * FROM bill WHERE clientID = %s', (name, ))
        return cursor.fetchall()
    except: 
        return False

def totalEarnings():
    try:
        cursor.execute('SELECT SUM(totalAmount) FROM bill')
        return cursor.fetchone()
    except: 
        return False


def todayEarnings():
    try:
        cursor.execute('SELECT SUM(totalAmount) FROM bill where date(dates) = %s ', (date.today(), ))
        return cursor.fetchall()
    except: 
        return False

def addcategory(arg):
    # print(arg)
    try:
        cursor.execute('INSERT into category (name) VALUES (%s)',arg)
        con.commit()
        return True
    except:
        return False

def addsubcategory(arg):
    # print(arg)
    try:
        cursor.execute('INSERT into subcategory (catName,name) VALUES (%s,%s)',arg)
        con.commit()
        return True
    except:
        return False
    
def category():
    try:
        cursor.execute('select id,name from category')
        return cursor.fetchall()
    except:
        return False

def subcategory():
    try:
        cursor.execute('select id,name from subcategory')
        return cursor.fetchall()
    except:
        return False

def checkquant(arg):
    print("Args = ",arg)
    try:
        cursor.execute('SELECT stock,Cost,id FROM product WHERE id=%s',(arg,))
        return cursor.fetchall()
    except:
        return False

def updateProductStock(arg,id):
    
    try:
        print("get",arg,id)
        cursor.execute('update product SET stock=%s where id=%s',(arg,id))
        con.commit()
        return True

    except:
        return False

def viewcategory():
    try:
        cursor.execute('SELECT * FROM category order by id desc')
        return cursor.fetchall()
    except:
        return False

def deletecategory(gup):
    try:
        cursor.execute('DELETE FROM category WHERE id = %s',gup)
        con.commit()
        return True

    except:
        return False

def selectcategory(arg):
    print("arsg = ",arg)
    try:
        cursor.execute('select * from category where id = %s',arg)
        return cursor.fetchall()
    except:
        return False

def updateCategory(arg):

    try:
        cursor.execute('update category SET name=%s where id=%s', arg)
        con.commit()
        return True
    except:
        return False


def allsubCategory():
    try:
        cursor.execute('SELECT subcategory.id, category.name, subcategory.name FROM subcategory left join category ON category.id = subcategory.catName')
        return cursor.fetchall()
    except:
        return False



def deleteSubCategory(gup):
    try:
        cursor.execute('DELETE FROM subcategory WHERE id = %s', gup)
        con.commit()
        return True
    except:
        return False

def singleSubcat(id):
    # print(id)
    # cursor.execute('SELECT category.id, category.name, subcategory.name FROM subcategory LEFT JOIN ON subcategory.catName = category.id WHERE subcategory.id = %s', id)
    try:
        cursor.execute('SELECT category.id, category.name, subcategory.name FROM subcategory LEFT JOIN category ON subcategory.catName = category.id WHERE subcategory.id = %s', id)
        return cursor.fetchone()
    except:
        return False


def updatesubCategory(arg):

    try:
        cursor.execute('update subcategory SET catName = %s,  name=%s where id=%s', arg)
        con.commit()
        return True
    except:
        return False
