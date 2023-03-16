from flask import Flask, render_template,jsonify 

app = Flask(__name__)

PRODUCTS=[
{
 'id' :1,
  'title':'Hero Cycle',
  'description':'HeroUrban Terrain UT7001S27.5  City Bike with Complete Accessories, Free Cycling Event & Ride Tracking App by Cultsport (Black - Blue, Ideal for Unisex, Frame: 18 Inches)',
  'price':2800,
  
}, 
{
 'id' :2,
  'title':'Tata Cycle',
  'description':'Tata Urban Terrain UT7001S27.5  City Bike with Complete Accessories, Free Cycling Event & Ride Tracking App by Cultsport (Black - Blue, Ideal for Unisex, Frame: 19 Inches)',
  'price':2500,
  
},
{
 'id' :3,
  'title':'Avon Cycle',
  'description':'Avon Urban Terrain UT7001S27.5  City Bike with Complete Accessories, Free Cycling Event & Ride Tracking App by Cultsport (Black - Blue, Ideal for Unisex, Frame: 18 Inches)',
  'price':6000,
  
}
  
]

@app.route('/')
def home():
  return render_template('home.html',products=PRODUCTS)


@app.route("/api/products")
def product_list():
  return jsonify(PRODUCTS)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
