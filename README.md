<p align="center">
  <img src="/icon.png" />
</p>

# alfred-fastlane

Select and execute Fastlane lanes directly from Alfred

https://user-images.githubusercontent.com/2648540/154819854-a76d8b81-644e-4e86-a662-fff7230281b1.mov

## Usage

### 1️⃣ Cache lanes first (required once per Fastlane project):
1) `Toggle Alfred`, type `fl`
3) `Select Fastlane project path` ↩︎
4) Select path ↩︎
5) `Cache lanes for …` ↩︎
6) A Terminal window will open. After caching is done, you can close the window.

https://user-images.githubusercontent.com/2648540/154820069-0fd35337-9934-4b9d-83c4-c36548ba6afe.mov

### 2️⃣ Select and execute lanes:
Repeat steps 1-4 from above
* Select and execute lane with ↩︎

#### With a lane selected, …
* hold ⌘ to toggle from `bundle exec fastlane [selected lane]` to `fastlane [selected lane]`
* hold ⌥ to add arguments to `bundle exec fastlane [selected lane]`
* hold ⇧ to add arguments to `fastlane [selected lane]`


https://user-images.githubusercontent.com/2648540/154820075-13395a91-a57c-4a63-b63c-5c20a70b23b9.mov


## PRO TIP:
If you primarily use a particular Fastlane project, it's **highly recommended** to set it as the default project path! If set, `fl` will already present all the lanes of your default project without having to select the path first ([see top video](#alfred-fastlane)).

The default project path can either be set
* in the settings (type `fl set`) or
* by repeating steps 1-4 from above and then selecting `Set [folder] as default project path` ↩︎

## This workflow utilizes:
* [alfred-fuzzy](https://github.com/deanishe/alfred-fuzzy) by Dean Jackson 
* [alfred-workflow](https://github.com/deanishe/alfred-workflow) by Dean Jackson
* Bootleg Fastlane logo by Marc Krenn

---

*Fastlane © Google, Inc. All Rights Reserved*

**This project is in no way endorsed, supported by or otherwise legally connected to Google, Inc.**
