# CASecureDashboard
-I wanted to create something to refresh my knowledge of building fullstack applications. I decided to build a single-page web dashboard that simulates monitoring internal infrastructure.


## Progress Tracker
##  Setup Phase
- [x] Installed and configured Node.js, NPM, Git, and curl
- [x] Created basic Express.js backend with /api/health and /api/logs
- [x] Built dynamic log storage system in Node backend
- [x] Created /api/push-log POST endpoint to accept new logs

##  Current Task
- [x] Test POST log injection manually using curl
- [x] Confirm logs are appearing via GET /api/logs

## Next Steps
- [x] Write Python script to simulate auto-log injection
- [ ] Write PowerShell script to simulate system health checks
- [ ] Create basic Vue.js frontend layout (Navbar, LogsView)
- [ ] Connect Vue frontend to backend API (Axios fetch)
- [ ] Display real-time logs on dashboard
- [ ] Deploy backend to AWS (optional bonus)

## Stretch Goals (if time allows)
- [ ] Add authentication to API routes
- [ ] Add service health check simulator using Kubernetes mock data
- [ ] Polish UI with responsive design
- [ ] Document project clearly for interview showcase

---

# Quick Commands Reference

## Run Backend
```bash
cd backend
node app.js
