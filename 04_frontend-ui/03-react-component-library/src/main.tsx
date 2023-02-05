import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import {
  Badge,
  Button,
  Input,
  Textarea,
  Checkbox,
  Radio,
  RadioGroup,
  Toggle,
  Avatar,
  Select,
  Spinner,
  ThemeProvider,
  useTheme,
} from "./index";
import "./tokens/colors.css";
import "./tokens/spacing.css";
import "./tokens/typography.css";
import "./demo.css";
import "@fontsource/inter/400.css";
import "@fontsource/inter/500.css";
import "@fontsource/inter/600.css";
import "@fontsource/inter/700.css";

const Demo = () => {
  // Form state for interactive examples
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [newsletter, setNewsletter] = useState(false);
  const [notifications, setNotifications] = useState(true);
  const [country, setCountry] = useState<string>("us");
  const [role, setRole] = useState<string>("member");
  const [avatarUrl, setAvatarUrl] = useState<string>(
    "https://i.pravatar.cc/150?img=1",
  );
  const { theme, setTheme } = useTheme();

  // Form validation
  const validateEmail = (value: string) => {
    if (!value) return "Email is required";
    if (!/\S+@\S+\.\S+/.test(value)) return "Email is invalid";
    return "";
  };

  const validatePassword = (value: string) => {
    if (!value) return "Password is required";
    if (value.length < 8) return "Password must be at least 8 characters";
    return "";
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setEmailError(validateEmail(email));
    setPasswordError(validatePassword(password));

    if (!emailError && !passwordError) {
      setIsLoading(true);
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 1500));
      setIsLoading(false);
      alert("Form submitted successfully!");
    }
  };

  return (
    <main className="demo">
      <header className="demo__header">
        <div>
          <div className="demo__brand">
            <img src="/pulsar.svg" alt="" aria-hidden="true" />
            <p className="demo__eyebrow">Pulsar UI</p>
          </div>
          <h1>Component Library Showcase</h1>
          <p className="demo__intro">
            Explore and interact with all components in the Pulsar UI library.
          </p>
        </div>
      </header>

      {/* Theme Toggle */}
      <div className="demo__theme-toggle">
        <label className="demo__field">
          <span>Theme:</span>
          <Toggle
            checked={theme === "dark"}
            onChange={(checked) => setTheme(checked ? "dark" : "light")}
          />
        </label>
        <Badge variant={theme === "dark" ? "info" : "success"}>
          {theme === "dark" ? "Dark Mode" : "Light Mode"}
        </Badge>
      </div>

      {/* Form Controls Section */}
      <section className="demo__panel" aria-labelledby="form-controls-heading">
        <div className="demo__section-heading">
          <div>
            <p className="demo__eyebrow">Form Controls</p>
            <h2 id="form-controls-heading">Interactive Form Elements</h2>
          </div>
        </div>
        <div className="demo__form-section">
          {/* Login Form Example */}
          <form onSubmit={handleSubmit} className="demo__login-form">
            <div className="demo__form-group">
              <label className="demo__field">
                <span>Email Address</span>
                <Input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  error={emailError}
                  leftAdornment={
                    emailError ? null : <span className="demo__icon">@</span>
                  }
                />
              </label>
              {emailError && <p className="demo__error-text">{emailError}</p>}
            </div>

            <div className="demo__form-group">
              <label className="demo__field">
                <span>Password</span>
                <Input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  error={passwordError}
                  leftAdornment={<span className="demo__icon">🔒</span>}
                  rightAdornment={
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => setPassword("")}
                      disabled={!password || isLoading}
                    >
                      Clear
                    </Button>
                  }
                />
              </label>
              {passwordError && (
                <p className="demo__error-text">{passwordError}</p>
              )}
            </div>

            <div className="demo__form-group">
              <Checkbox
                checked={newsletter}
                onChange={(e) => setNewsletter(e.target.checked)}
                label="Subscribe to newsletter"
              />
            </div>

            <div className="demo__form-actions">
              <Button
                variant="primary"
                type="submit"
                loading={isLoading}
                disabled={isLoading}
              >
                Sign In
              </Button>
              <Button variant="secondary" type="button">
                Forget Password?
              </Button>
            </div>
          </form>

          {/* Additional Controls Demo */}
          <div className="demo__additional-controls">
            <div className="demo__control-group">
              <label className="demo__field">
                <Select
                  label="Country"
                  options={[
                    { value: "", label: "Select country" },
                    { value: "us", label: "United States" },
                    { value: "uk", label: "United Kingdom" },
                    { value: "ca", label: "Canada" },
                    { value: "au", label: "Australia" },
                  ]}
                  value={country}
                  onChange={(value) => setCountry(value)}
                  placeholder="Select country"
                />
              </label>
            </div>

            <div className="demo__control-group">
              <fieldset className="demo__radio-group">
                <legend className="demo__field">
                  <span>User Role</span>
                </legend>
                <RadioGroup
                  name="user-role"
                  value={role}
                  onChange={(value: string) => setRole(value)}
                >
                  <div className="demo__radio-options">
                    <label className="demo__field demo__radio-label">
                      <Radio value="member" label="Member" />
                    </label>
                    <label className="demo__field demo__radio-label">
                      <Radio value="admin" label="Administrator" />
                    </label>
                    <label className="demo__field demo__radio-label">
                      <Radio value="moderator" label="Moderator" />
                    </label>
                  </div>
                </RadioGroup>
              </fieldset>
            </div>

            <div className="demo__control-group">
              <label className="demo__field">
                <span>Notifications</span>
                <Toggle
                  checked={notifications}
                  onChange={(checked) => setNotifications(checked)}
                  label="Enable email notifications"
                />
              </label>
            </div>
          </div>
        </div>
      </section>

      {/* Data Display Section */}
      <section className="demo__panel" aria-labelledby="data-display-heading">
        <div className="demo__section-heading">
          <div>
            <p className="demo__eyebrow">Data Display</p>
            <h2 id="data-display-heading">Avatars, Badges & Indicators</h2>
          </div>
        </div>
        <div className="demo__display-section">
          {/* Avatar Examples */}
          <div className="demo__avatar-examples">
            <h3>Avatars</h3>
            <div className="demo__avatar-group">
              <Avatar
                src={avatarUrl}
                alt="User Avatar"
                fallback="UA"
                size="xs"
              />
              <Avatar
                src={avatarUrl}
                alt="User Avatar"
                fallback="UA"
                size="sm"
              />
              <Avatar
                src={avatarUrl}
                alt="User Avatar"
                fallback="UA"
                size="md"
              />
              <Avatar
                src={avatarUrl}
                alt="User Avatar"
                fallback="UA"
                size="lg"
              />
              <Avatar
                src={avatarUrl}
                alt="User Avatar"
                fallback="UA"
                size="xl"
              />
            </div>
          </div>

          {/* Badge Examples */}
          <div className="demo__badge-examples">
            <h3>Badges</h3>
            <div className="demo__badge-group">
              <Badge variant="success">Success</Badge>
              <Badge variant="info">Info</Badge>
              <Badge variant="warning">Warning</Badge>
              <Badge variant="error">Error</Badge>
            </div>
          </div>

          {/* Notification Example */}
          <div className="demo__notification-example">
            <h3>Notification Indicator</h3>
            <Button
              variant="ghost"
              size="lg"
              className="demo__notification-btn"
            >
              <span className="demo__icon">🔔</span>
              <Badge variant="error" dot>
                9+
              </Badge>
            </Button>
          </div>
        </div>

        <div className="demo__display-section">
          <div className="demo__avatar-examples">
            <h4>Fallbacks</h4>
            <div className="demo__avatar-group demo__avatar-fallbacks">
              <Avatar alt="JD" fallback="JD" size="md" />
              <Avatar alt="Maria Garcia" fallback="MG" size="md" />
              <Avatar alt="🚀" fallback="🚀" size="md" />
              <Avatar
                alt="Broken Image"
                fallback="BI"
                src="invalid-image-url.jpg"
                size="md"
              />
            </div>
          </div>

          <div className="demo__badge-examples">
            <h4>Sizes & States</h4>
            <div className="demo__badge-group demo__badge-variants">
              <Badge variant="info" size="sm">
                Small
              </Badge>
              <Badge variant="info" size="md">
                Medium
              </Badge>
            </div>
          </div>

          {/* Notification Example */}
          <div className="demo__notification-example"></div>
        </div>
      </section>

      {/* Button Showcase */}
      <section
        className="demo__panel"
        aria-labelledby="button-showcase-heading"
      >
        <div className="demo__section-heading">
          <div>
            <p className="demo__eyebrow">Actions</p>
            <h2 id="button-showcase-heading">Button Variants & States</h2>
          </div>
        </div>
        <div className="demo__button-showcase">
          {/* Button Variants */}
          <div className="demo__button-group">
            <h3>Variants</h3>
            <Button variant="primary">Primary</Button>
            <Button variant="secondary">Secondary</Button>
            <Button variant="ghost">Ghost</Button>
            <Button variant="danger">Danger</Button>
          </div>

          {/* Button Sizes */}
          <div className="demo__button-group">
            <h3>Sizes</h3>
            <Button variant="primary" size="sm">
              Small
            </Button>
            <Button variant="primary" size="md">
              Medium
            </Button>
            <Button variant="primary" size="lg">
              Large
            </Button>
          </div>

          {/* Button States */}
          <div className="demo__button-group">
            <h3>States</h3>
            <Button variant="primary" disabled>
              Disabled
            </Button>
            <Button variant="primary" loading>
              Loading
            </Button>
            <Button variant="primary" loading>
              Loading...
            </Button>
          </div>

          {/* Button with Icons */}
          <div className="demo__button-group">
            <h3>With Icons</h3>
            <Button
              variant="primary"
              leftIcon={<span className="demo__icon">📧</span>}
            >
              Send Email
            </Button>
            <Button
              variant="secondary"
              rightIcon={<span className="demo__icon">→</span>}
            >
              Learn More
            </Button>
            <Button
              variant="ghost"
              leftIcon={<span className="demo__icon">✓</span>}
              rightIcon={<span className="demo__icon">→</span>}
            >
              Confirm
            </Button>
          </div>
        </div>
        {/* Full Width Button */}
        <Button variant="primary" fullWidth>
          Full Width Button
        </Button>
      </section>

      {/* Textarea & Miscellaneous */}
      <section className="demo__panel" aria-labelledby="misc-heading">
        <div className="demo__section-heading">
          <div>
            <p className="demo__eyebrow">Additional Components</p>
            <h2 id="misc-heading">Textarea & Spinner</h2>
          </div>
        </div>
        <div className="demo__misc-section">
          <div className="demo__textarea-demo">
            <label className="demo__field">
              <span>Bio</span>
              <Textarea placeholder="Tell us about yourself..." rows={4} />
            </label>
          </div>

          <div className="demo__spinner-demo">
            <h3>Spinners</h3>
            <div className="demo__spinner-group">
              <Spinner size="sm" color="currentColor" />
              <Spinner size="md" color="currentColor" />
              <Spinner size="lg" color="currentColor" />
            </div>

            <div className="demo__spinner-group demo__spinner-colored">
              <Spinner size="md" color="#2563eb" />
              <Spinner size="md" color="#10b981" />
              <Spinner size="md" color="#f59e0b" />
              <Spinner size="md" color="#ef4444" />
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="demo__footer">
        <p>Pulsar UI &mdash; Component Library</p>
      </footer>
    </main>
  );
};

createRoot(document.getElementById("root")!).render(
  <ThemeProvider>
    <React.StrictMode>
      <Demo />
    </React.StrictMode>
  </ThemeProvider>,
);
