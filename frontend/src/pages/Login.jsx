import { useState } from 'react';
import SchoolLogin from '../components/login/SchoolLogin.jsx';
import OtherLogin from '../components/login/OtherLogin.jsx';
import '../App.css';
import style from '../components/login/login.module.css';

export default function Login() {
    const [tab, setTab] = useState('school');

    return (
        <div className={style.background}>
            <div className='login-screen'>
            <div className='login-tabs'>
                <button
                    onClick={() => setTab('school')}
                    style={{
                        padding: '0.5rem 1rem',
                        background: tab === 'school' ? '#222' : '#eee',
                        color: tab === 'school' ? '#fff' : '#222',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer'
                    }}
                >
                    School Login
                </button>
                <button
                    onClick={() => setTab('other')}
                    style={{
                        padding: '0.5rem 1rem',
                        background: tab === 'other' ? '#222' : '#eee',
                        color: tab === 'other' ? '#fff' : '#222',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer'
                    }}
                >
                    Other Login
                </button>
            </div>
            {tab === 'school' ? <SchoolLogin /> : <OtherLogin />}
            </div>
        </div>
    );
}