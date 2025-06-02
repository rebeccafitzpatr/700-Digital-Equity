{ pkgs }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    python312Packages.pip
    python312Packages.flask
    python312Packages.flask_cors
    iputils  # Provides `ping`
    nodejs_20
    nodePackages.vite
  ];
}
