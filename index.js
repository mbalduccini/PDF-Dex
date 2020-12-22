const { Client } = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200' })

const init = async ()  => {
    
    const result = await client.search({
        index: 'pdfs',
        body: {
            "query": {
                "range": {
                    // Finds all articles where word
                    // "regulatory" appears at least once.
                    "tokenized_words.regulatory": {
                        "gte": 1
                    }
                }
            }
        }
    });

    console.log(JSON.stringify(result.body, null, 2));
}

init();
