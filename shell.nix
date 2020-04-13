{ pkgs ? import <nixpkgs> {} }:

with pkgs;

poetry2nix.mkPoetryEnv {
  python = python38;
  projectDir = ./.;
}
