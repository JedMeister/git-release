git-release
===========

Check for releases/tags of projects hosted on GitHub, GitLab, Gitea or Forgejo
git servers.

IMPORTANT
---------

At the time of writing this project is a plan/idea and is currently
non-functional...

---

At it's core, git-releases is intended as a python3 rewrite of [gh_releases][1]
- with some code robbed from; and inspired by [octohub][2].

Initially it is designed as a drop-in replacement for gh_releases - i.e. get
release/tag info from projects hosted on [GitHub][3].

Once that has been completed support for [Forgejo][4] will be next on the dev
roadmap - both [Codeburg][5] & self hosted.

As Forgejo is a fork of [Gitea][6], it should also work with Gitea, but testing
that will not be high priority.

Once Forgejo is supported, [GitLab][7] will be next in line. As per Forgejo
support, the aim will be for it to work with both hosted and self-hosted
GitLab.

Additional functionality is planned (hoped?!) for the future. Some ideas for
future development:

- support for downloading & verification of  code/binaries/keys - i.e.:
  - Git clones
  - Download build assets - e.g. tarballs, binaries, installers, etc.
  - Download verification keys/checksums.
  - Verify assets against keys/checksums.
  - Other git server functionality?!

[1]: https://github.com/turnkeylinux/common/blob/18.x/overlays/turnkey.d/github-latest-release/usr/local/bin/gh_releases
[2]: https://github.com/turnkeylinux/octohub
[3]: https://github.com/
[4]: https://forgejo.org/
[5]: https://codeberg.org/
[6]: https://gitea.com/
[7]: https://gitlab.com/
