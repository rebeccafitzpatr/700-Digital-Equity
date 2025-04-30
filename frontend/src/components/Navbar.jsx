import React from "react"
import { Link } from "react-router-dom"

export default function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <Link to="/">Home</Link>
            </div>
            <ul className="navbar-links">
                <li>
                <Link to="/login">Login</Link>
                </li>
                <li>
                <Link to="/comparison">Leaderboard</Link>
                </li>

            </ul>
            </nav>
    )
}