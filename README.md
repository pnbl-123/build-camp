# Firebase AI Template

## Product Overview

### Core functionality

Template for a Firebase AI project.

### Key Features

Firebase Authentication (Google Sign-in)

Firebase Hosting

Firebase Functions

Firebase AI (Google Gemini AI via Vertex AI)

## Technical Design

### Technology Stack
- Frontend: React.js
- Backend: Firebase Services
- Database: Firestore
- Authentication: Firebase Authentication (Google Sign-in)
- AI Integration: Google Gemini AI via Vertex AI
- Hosting: Firebase Hosting

### Project Structure

```
project/
│
├── client/
│ ├── public/
│ │ ├── index.html
│ │ └── manifest.json
│ ├── src/
│ │ ├── pages/
│ │ │ ├── Home.js
│ │ │ ├── Home.css
│ │ │ ├── Login.js
│ │ │ └── Login.css
│ │ ├── App.js
│ │ ├── App.css
│ │ └── index.js
│ ├── package.json
│ └── .env
│
├── firebase.json
├── .firebaserc
└── README.md
```

### Setup Instructions

#### Prerequisites
- Node.js (v20 or later)
- npm (v10 or later)
- Firebase CLI (`npm install -g firebase-tools`)
- Google Cloud account with Firebase project

#### Frontend Setup

1. Clone the repository and navigate to the client directory:
   ```bash
   cd client
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the client directory with your Firebase configuration:
   ```
   REACT_APP_FIREBASE_API_KEY=your_api_key
   REACT_APP_FIREBASE_AUTH_DOMAIN=your_auth_domain
   REACT_APP_FIREBASE_PROJECT_ID=your_project_id
   REACT_APP_FIREBASE_STORAGE_BUCKET=your_storage_bucket
   REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
   REACT_APP_FIREBASE_APP_ID=your_app_id
   ```

4. Start the development server:
   ```bash
   npm start
   ```

### Firebase Configuration

1. Enable Google Authentication in Firebase Console:
   - Go to Firebase Console > Authentication > Sign-in method
   - Enable Google sign-in provider
   - Configure OAuth consent screen if needed

2. Deploy to Firebase:
   ```bash
   firebase login
   firebase init
   firebase deploy
   ```

### Features
- Google Authentication
- Protected Routes
- Responsive Design
- User Profile Display
- Secure Sign Out

### Development Workflow

1. Make changes to the frontend code in the `client/src` directory
2. Test changes locally using `npm start`
3. Build the production version using `npm run build`
4. Deploy to Firebase using `firebase deploy`

### Available Scripts

In the client directory, you can run:

- `npm start` - Runs the app in development mode
- `npm run build` - Builds the app for production

### Environment Variables

Required environment variables in `.env`:
```
REACT_APP_FIREBASE_API_KEY
REACT_APP_FIREBASE_AUTH_DOMAIN
REACT_APP_FIREBASE_PROJECT_ID
REACT_APP_FIREBASE_STORAGE_BUCKET
REACT_APP_FIREBASE_MESSAGING_SENDER_ID
REACT_APP_FIREBASE_APP_ID
```

### License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.