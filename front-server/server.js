const express =require('express')
const path = require('path')

// server settings
const host = "client"
const port = 3000
const rootDir = String(process.cwd() + "/")

const app = express()

// static route 
app.use('/static', express.static(path.join(rootDir, 'staticfiles', 'static')))

app.use('/favicon', express.static(path.join(rootDir, 'favicon')))

// vue app route
app.get('*', (req, res) => {
    try {
        res.sendFile(path.join(rootDir, 'staticfiles', 'index.html'))
    } catch (e) {
        res.status(500).send({status: 500, error: e})
    }
})

// run server
app.listen(
    port,
    host,
    (err) => {
        if(err) {
            return console.log(err)
        }
        return console.log(`Front server started on ${host}:${port}`)
    }
)