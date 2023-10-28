```javascript
import next from 'next';
import express from 'express';
import { InterviewService } from '../services/InterviewService';
import { NarrativeService } from '../services/NarrativeService';
import { UserService } from '../services/UserService';
import { PerformanceService } from '../services/PerformanceService';
import { FeedbackService } from '../services/FeedbackService';
import { errorHandlingMiddleware } from '../middleware/errorHandlingMiddleware';
import { authenticationMiddleware } from '../middleware/authenticationMiddleware';
import { performanceOptimizationMiddleware } from '../middleware/performanceOptimizationMiddleware';
import { feedbackMiddleware } from '../middleware/feedbackMiddleware';

const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();

  server.use(express.json());
  server.use(authenticationMiddleware);
  server.use(performanceOptimizationMiddleware);
  server.use(feedbackMiddleware);

  server.get('/api/interview', InterviewService.getInterview);
  server.post('/api/interview', InterviewService.createInterview);
  server.put('/api/interview/:id', InterviewService.updateInterview);
  server.delete('/api/interview/:id', InterviewService.deleteInterview);

  server.get('/api/narrative', NarrativeService.getNarrative);
  server.post('/api/narrative', NarrativeService.createNarrative);
  server.put('/api/narrative/:id', NarrativeService.updateNarrative);
  server.delete('/api/narrative/:id', NarrativeService.deleteNarrative);

  server.get('/api/user', UserService.getUser);
  server.post('/api/user', UserService.createUser);
  server.put('/api/user/:id', UserService.updateUser);
  server.delete('/api/user/:id', UserService.deleteUser);

  server.get('/api/performance', PerformanceService.getPerformance);
  server.post('/api/performance', PerformanceService.createPerformance);
  server.put('/api/performance/:id', PerformanceService.updatePerformance);
  server.delete('/api/performance/:id', PerformanceService.deletePerformance);

  server.get('/api/feedback', FeedbackService.getFeedback);
  server.post('/api/feedback', FeedbackService.createFeedback);
  server.put('/api/feedback/:id', FeedbackService.updateFeedback);
  server.delete('/api/feedback/:id', FeedbackService.deleteFeedback);

  server.get('*', (req, res) => {
    return handle(req, res);
  });

  server.use(errorHandlingMiddleware);

  server.listen(3000, (err) => {
    if (err) throw err;
    console.log('> Ready on http://localhost:3000');
  });
}).catch((ex) => {
  console.error(ex.stack);
  process.exit(1);
});
```