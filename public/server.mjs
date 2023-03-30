import express from 'express'
import path from 'path'
import { fileURLToPath } from 'url'
import child_process from 'child_process'
import { WebSocketServer } from 'ws'
import http from 'http'


// Function to run an external process and call a function for each line of its output
function captureExternalProcess(command, parameterArray, lineHandler, cwd) {
  // Received data buffer
  let received = '';
  
  // Start the child process
  console.log('Running external process...');
  let externalProcess = child_process.spawn(command, parameterArray, {cwd: cwd});
  
  // Handle output from the child process
  externalProcess.stdout.on('data', (data) => {
    // Add received characters to input buffer
    received = received.concat(data);
    // Split off any full lines received
    for (;;) {
      const lineEnd = received.indexOf('\n')
      if (lineEnd < 0) break;
      const line = received.slice(0, lineEnd).trim();
      received = received.slice(lineEnd + 1);
      lineHandler(line);
    }
  });
  
  // Handle child process terminating
  externalProcess.on('exit', (result) => {
    console.log('WARNING: External process exited: ' + result);
    externalProcess = null;
  });
  
  // Kill child process when we exit
  process.on('SIGINT', () => process.exit());
  process.on('SIGTERM', () => process.exit());
  process.on('exit', function() {
    if (externalProcess) {
      console.log('Stopping external process...');
      externalProcess.kill();
    }
  });  
}

function broadcast(message) {
  for (const ws of wss.clients) {
    ws.send(message)
  }
}


const currentFolder = path.dirname(fileURLToPath(import.meta.url))

const app = express()
const server = http.Server(app)
//const wss = new WebSocketServer({ server: server, path: '/ws', clientTracking: true })
const wss = new WebSocketServer({ port: 3001, path: '/ws', clientTracking: true })

wss.on('connection', function(ws) {
  console.log('New connection')
  ws.on('message', function(message) {
    console.log('Received: ', message)
    //ws.send('I heard: ' + message)
  })
})

// app.get('/', (req, res) => {
//   res.sendFile(path.join(currentFolder, 'websocket.html'))
// })


app.use('/', express.static(path.join(currentFolder, 'public')))

app.listen(3000, () => {
  console.log('Listening at http://localhost:3000')
})

//let counter = 0; setInterval(() => { broadcast(++counter) }, 1000)

// Run the external process, handle each received line
captureExternalProcess('python3', [path.join(currentFolder, '..', 'Mistys_Adventure.py')], (line) => {
  //const value = parseFloat(line)
  console.log('RECV: ' + line);
  broadcast(line);
}, path.join(currentFolder, '..'));
