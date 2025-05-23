
export default function OtherLogin() {
    return (
        <div>
            <h1>Other Login</h1>
            <form>
                <div>
                    <label htmlFor="other-username">Username:</label>
                    <input type="text" id="other-username" name="username" required />
                </div>
                <div>
                    <label htmlFor="other-password">Password:</label>
                    <input type="password" id="other-password" name="password" required />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}