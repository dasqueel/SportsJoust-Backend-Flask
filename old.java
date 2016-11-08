//post outcome and data to mpostMatch
    protected void postOutcome(final String contest, final JSONObject postJson, final String mtoken,final String outcome) {
        Thread t = new Thread() {

            public void run() {
                Looper.prepare(); //For Preparing Message Pool for the child Thread
                HttpClient client = new DefaultHttpClient();
                HttpConnectionParams.setConnectionTimeout(client.getParams(), 10000); //Timeout Limit
                HttpResponse response;
                JSONObject json = new JSONObject();

                try {
                    HttpPost post = new HttpPost("http://52.24.226.232/mpostMatch");
                    //postJson.put("contest", contest);
                    postJson.put("contest", contest);
                    postJson.put("mtoken", mtoken);
                    postJson.put("outcome", outcome);
                    StringEntity se = new StringEntity( postJson.toString()); //or json.toString()
                    se.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                    post.setEntity(se);
                    response = client.execute(post);
                    //Log.i("postJson",postJson.toString());

                    /*Checking response */
                    if(response!=null){
                        InputStream in = response.getEntity().getContent(); //Get the data in the entity
                        String resp = readString(in);
                        Log.i("post",resp);
                        displayMatch(postJson);
                    }

                } catch(Exception e) {
                    e.printStackTrace();
                    //createDialog("Error", "Cannot Estabilish Connection");
                }

                Looper.loop(); //Loop in the message queue
            }
        };

        t.start();
    }

//function to read opst response
    public static String readString(InputStream inputStream) throws IOException {

        ByteArrayOutputStream into = new ByteArrayOutputStream();
        byte[] buf = new byte[4096];
        for (int n; 0 < (n = inputStream.read(buf));) {
            into.write(buf, 0, n);
        }
        into.close();
        return new String(into.toByteArray(), "UTF-8"); // Or whatever encoding
    }

/*
 private void makeJsonObjectRequest(String url) {

     JsonObjectRequest jsonObjReq = new JsonObjectRequest(Method.POST,
             url, null, new Response.Listener<JSONObject>() {

         @Override
         public void onResponse(JSONObject response) {
             Log.d(TAG, response.toString());

             try {
                 // Parsing json object response
                 // response will be a json object
                 String passed = response.getString("passed");
                 //String bal = response.getString("bal");

                 if (passed.equals("yes"))
                 {
                     //set session
                     SharedPreferences.Editor editor = sharedpreferences.edit();
                     String u = userName.getText().toString();
                     String p = pwd.getText().toString();
                     editor.putString("userName", u);
                     editor.putString("pwd", p);
                     //editor.putString("bal",bal);
                     editor.commit();
                     //switch to home screen
                     Intent myIntent = new Intent(MainActivity.this, Home.class);
                     startActivity(myIntent);


                 } else if (passed.equals("no un")){
                     Toast.makeText(getApplicationContext(),"username not registered",Toast.LENGTH_LONG).show();
                 } else {
                     Toast.makeText(getApplicationContext(),"incorrect password",Toast.LENGTH_LONG).show();
                 }

             } catch (JSONException e) {
                 e.printStackTrace();
                 Toast.makeText(getApplicationContext(),
                         "Error: " + e.getMessage(),
                         Toast.LENGTH_LONG).show();
             }
         }
     }, new Response.ErrorListener() {

         @Override
         public void onErrorResponse(VolleyError error) {
             VolleyLog.d(TAG, "Error: " + error.getMessage());
             Toast.makeText(getApplicationContext(),
                     error.getMessage(), Toast.LENGTH_SHORT).show();
         }
     });

     // Adding request to request queue
     AppController.getInstance().addToRequestQueue(jsonObjReq);
 }*/