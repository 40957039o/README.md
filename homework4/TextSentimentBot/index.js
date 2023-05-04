'use strict';
const line = require('@line/bot-sdk'),
      express = require('express'),
      configGet = require('config');
const {TextAnalyticsClient, AzureKeyCredential} = require("@azure/ai-text-analytics");

//Line config
const configLine = {
  channelAccessToken:configGet.get("CHANNEL_ACCESS_TOKEN"),
  channelSecret:configGet.get("CHANNEL_SECRET")
};

//Azure Text Sentiment
const endpoint = configGet.get("ENDPOINT");
const apiKey = configGet.get("TEXT_ANALYTICS_API_KEY");

const client = new line.Client(configLine);
const app = express();

const port = process.env.PORT || process.env.port || 3000;

app.listen(port, ()=>{
  console.log(`listening on ${port}`);
   
});

async function MS_TextSentimentAnalysis(thisEvent){
    console.log("[MS_TextSentimentAnalysis] in");
    const analyticsClient = new TextAnalyticsClient(endpoint, new AzureKeyCredential(apiKey));
    let documents = [];
    documents.push(thisEvent.message.text);

    const results = await analyticsClient.analyzeSentiment(documents);
    console.log("[results] ", JSON.stringify(results));

    const sentiment = results[0].sentiment;
    let echo;
      if(sentiment === 'positive'){
        echo = { type: 'text', text: '這是正向的訊息' };
      } else if(sentiment === 'negative') {
        echo = { type: 'text', text: '這是負向的訊息' };
      } else {
        echo = { type: 'text', text: '這是中性的訊息' };
      }
    const confi = {
      type: 'text',
      text: `正向分數: ${results[0].confidenceScores.positive.toFixed(2)}, 負向分數: ${results[0].confidenceScores.negative.toFixed(2)}, 中性分數: ${results[0].confidenceScores.neutral.toFixed(2)}`
    };

      return client.replyMessage(thisEvent.replyToken, [echo,confi]);

}

app.post('/callback', line.middleware(configLine),(req, res)=>{
  Promise
    .all(req.body.events.map(handleEvent))
    .then((result)=>res.json(result))
    .catch((err)=>{
      console.error(err);
      res.status(500).end();
    });
});

function handleEvent(event){
  if(event.type !== 'message' || event.message.type !== 'text'){
    return Promise.resolve(null);
  }

  MS_TextSentimentAnalysis(event)
    .catch((err) => {
      console.error("Error:", err);
    }); 
}