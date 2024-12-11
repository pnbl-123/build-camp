import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getAuth, signOut } from 'firebase/auth';
import './Home.css';

function Home() {
  const auth = getAuth();
  const navigate = useNavigate();
  const user = auth.currentUser;

  useEffect(() => {
    if (!user) {
      navigate('/login');
    }
  }, [user, navigate]);

  const handleLogout = async () => {
    try {
      await signOut(auth);
      navigate('/login');
    } catch (error) {
      console.error('Error signing out:', error);
    }
  };

  if (!user) return null;

  return (
    <div className="home-container">
      <h1>Welcome, {user.displayName}!</h1>
      <img src={user.photoURL} alt="Profile" className="profile-image" />
      <p>You are signed in with: {user.email}</p>
      <button onClick={handleLogout} className="logout-btn">
        Sign Out
      </button>
    </div>
  );
}

export default Home; 