

// use d3 json to access the Flask API data 
// use list of data to populate
d3.json('http://127.0.0.1:5000/api/v1.0/data_science_data').then((data) => {
    console.log(data)
})

const headers = {'Content-Type':'application/json',
'Access-Control-Allow-Origin':'*',
'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'}
const response = {
statusCode: 200,
headers:headers,
body: JSON.stringify(X),
};
//return response;